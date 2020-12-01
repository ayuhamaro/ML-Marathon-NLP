observations = ('dry', 'dry', 'dry')
states = ('sunny', 'rainy')
start_probability = {'sunny': 0.4, 'rainy': 0.6}
transition_probability = {'sunny': {'sunny': 0.6, 'rainy': 0.4},
                          'rainy': {'sunny': 0.3, 'rainy': 0.7}}
emission_probatility = {'sunny': {'dry': 0.6, 'damp': 0.3, 'soggy': 0.1},
                        'rainy': {'dry': 0.1, 'damp': 0.4, 'soggy': 0.5}}


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for cur_state in states:
            (prob, state) = max(
                [(V[t - 1][pre_state] * trans_p[pre_state][cur_state] * emit_p[cur_state][obs[t]], pre_state) for
                 pre_state in states])
            V[t][cur_state] = prob
            newpath[cur_state] = path[state] + [cur_state]

        path = newpath

    (prob, state) = max([(V[len(obs) - 1][final_state], final_state) for final_state in states])
    return (prob, path[state])


result = viterbi(observations,
                 states,
                 start_probability,
                 transition_probability,
                 emission_probatility)


print(result)