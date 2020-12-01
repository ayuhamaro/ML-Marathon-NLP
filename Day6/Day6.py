import pandas as pd
import jieba

pd_corpus = pd.read_csv('ChnSentiCorp_htl_all.csv')
pd_corpus.head(5)

print(pd_corpus)

pd_positive = pd_corpus.loc[pd_corpus['label'] == 1, :]
pd_negative = pd_corpus.loc[pd_corpus['label'] == 0, :]

print(f'Total: {len(pd_corpus)}, Positive: {len(pd_positive)}, Negative: {len(pd_negative)}')

pd_corpus.dropna(inplace=True)

class JiebaCutingClass(object):
    def __init__(self, key_to_cut: str, dic: str = None, userdict: str = None):
        if dic is not None:
            jieba.set_dictionary(dic)

        if userdict is not None:
            jieba.load_userdict(userdict)

        self.key_to_cut = key_to_cut

        jieba.enable_paddle()

    @staticmethod
    def cut_single_sentence(sentence, use_paddle=False, use_full=False, use_search=False):

        if use_search:
            out = jieba.cut_for_search(sentence)
        else:
            out = jieba.cut(sentence, use_paddle=use_paddle, cut_all=use_full)

        return out

    def cut_corpus(self, corpus: pd.DataFrame, mode: str) -> pd.DataFrame:
        if mode not in ['paddle', 'full', 'precise', 'search']:
            raise TypeError(f'only support `paddle`, `full`, `precise`, and `search` mode, but get {mode}')

        if mode == 'paddle':
            out = self._paddle_cut(corpus)
        elif mode == 'full':
            out = self._full_cut(corpus)
        elif mode == 'precise':
            out = self._precise_cut(corpus)
        elif mode == 'search':
            out = self._search_cut(corpus)

        return out

    def _paddle_cut(self, corpus):
        jieba.enable_paddle()

        out = []
        for single_review in corpus[self.key_to_cut]:
            out.append([word for word in JiebaCutingClass.cut_single_sentence(single_review, use_paddle=True)])

        corpus['cut'] = out

        return corpus

    def _full_cut(self, corpus):
        out = []
        for single_review in corpus[self.key_to_cut]:
            out.append([word for word in JiebaCutingClass.cut_single_sentence(single_review, use_full=True)])

        corpus['cut'] = out

        return corpus

    def _precise_cut(self, corpus):
        out = []
        for single_review in corpus[self.key_to_cut]:
            out.append([word for word in JiebaCutingClass.cut_single_sentence(single_review)])

        corpus['cut'] = out

        return corpus

    def _search_cut(self, corpus):
        out = []
        for single_review in corpus[self.key_to_cut]:
            out.append([word for word in JiebaCutingClass.cut_single_sentence(single_review, use_search=True)])

        corpus['cut'] = out

        return corpus


jieba_cut = JiebaCutingClass(key_to_cut='review')
pd_cut = jieba_cut.cut_corpus(pd_corpus.loc[:10, :], mode='precise')

pd_cut.head()

print(pd_cut)


test_string = '我愛cupoy自然語言處理馬拉松課程'

jieba_cut = JiebaCutingClass(key_to_cut='', dic='dict.txt.big')
out_string = jieba_cut.cut_single_sentence(test_string, use_paddle=True)
print(f'Paddle模式: {[string for string in out_string]}')

out_string = jieba_cut.cut_single_sentence(test_string, use_full=True)
print(f'全模式: {[string for string in out_string]}')

out_string = jieba_cut.cut_single_sentence(test_string, use_search=True)
print(f'搜尋模式: {[string for string in out_string]}')

out_string = jieba_cut.cut_single_sentence(test_string)
print(f'精確模式: {[string for string in out_string]}')
