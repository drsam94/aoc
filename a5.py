PART = 1
alph = list(map(chr,range(ord('a'), ord('z') + 1)))
if PART == 1:
    print(sum((
          any(c + c in w for c in alph) and
          sum(w.count(v) for v in 'aeiou') >= 3 and
          all (b not in w for b in ['ab','cd','pq','xy'])) for w in open('a5.in')))
elif PART == 2:
    print(sum((
          any(w.count(a + b) > 1 for a in alph for b in alph) and
          any(a + b + a in w for a in alph for b in alph)) for w in open('a5.in')))
