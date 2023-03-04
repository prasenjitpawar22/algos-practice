# find all the occurances of p in t (KMP algo)
p = 'aas'
t = 'aaaaasdasasasaassaassaaassaas'

# build the lps of - p
# len will be = p's len
lps = [0] * len(p)
count = 0
# prevLPS pointer => 0 => lps[0] starting postion
# i => 1 pointer to current lps - i.e next to prevLPS
prevLPS, i = 0, 1
# while i-current is less then length of p
while i < len(p):
  # check if current pointer -> i
  # matches with prev pointer prevLPS -> p index
  if (p[i] == p[prevLPS]):
    # then lsp of i - current value will be
    # prevLPS pointer value + 1
    lps[i] += prevLPS + 1
    # e.g
    #           0  1  2  3
    # - p   -> [A, A, A, X]  -> here A = A 
    # - lps -> [0, ?, 0, 0] so ? will be set to 1 -> i.e prevLPS+1
    # -         ^  ^
    # -   prevLPS  i     
    # -        
    #           0  1  2  3
    # - p   -> [A, A, A, X]  -> here A = A 
    # - lps -> [0, 1, ?, 0] so ? will be set to 2 -> i.e prevLPS+1
    # -            ^  ^
    # -      prevLPS  i     and for next iteration A != X, shift to else condition
    # -      
    # then prevLPS pointer shift to by +1
    # and i - current shift by +1 
    prevLPS += 1
    i += 1
  # if no match then
  else:
    if prevLPS == 0:
      # handle condition when prevLPS pointer is 0
      # e.g
      # - p   -> [A, B]
      # - lps -> [0, ?]
      # -         ^  ^
      # -         |  |
      # -   prevLPS  i
      # here prevLPS is 0 can't shift to left anymore
      # so vlaue to be inserted at current i - lsp[i] will
      # be lsp[prevLPS] also could just insert 0,
      # and just shift the i pointer to next so, the solution
      # - p   -> [A, B]
      # - lps -> [0, 0]
      # -         ^  ^
      # -         |  |
      # -   prevLPS  i
      lps[i] = lps[prevLPS] #lps[i] = lps[prevLPS] 
      i += 1
    else:
      # what if prevLPS not 0 then
      # e.g       1  2  3  4
      # - p   -> [A, A, A, X]
      # - lps -> [0, 1, 2, ?]
      # -               ^  ^
      # -               |  |
      # -          prevLPS i
      # here prevLPS is at index 2 NOTE: not the actual value 2
      # but index 3 so, we need to shift the prevLPS right but how
      # simple just shift it by the value of lps[prevLPS-1]
      # Note: not just shift it left like prevLPS = prevLPS - 1 !!
      prevLPS = lps[prevLPS - 1]

# now traverse the string
i, j = 0, 0
while i < len(t):
  if t[i] == p[j]:
    # just increase the i j
    i, j = i + 1, j + 1
  else:
    # for eg.
    #       012  0123456789
    #       sda  sadasdesda
    #         ^        ^
    #         j !=     i
    # here a != e so, need to shift j right but how
    #
    if j == 0:
      #just increse the i pointer
      i += 1
    # elif j==len(t)
    
    else:
      # j pointer shift buy the value of lps[j-1]
      # and no need to shift the i pointer
      # the above if state will take care of it
      # here's how the above example will playout
      #       012  0123456789
      #       sda  sadasdesda
      #         ^        ^                  2       2-1
      #         j !=     i -> lps[0,0,0] -> j = lps[j-1] -> j = 0
      #
      # as j = 0 and can't be futher shifted to lift
      # the above if statemet take care of it!
      j = lps[j - 1]

  # as per the problem statement we have to check all the
  # occurences of p in t for that
  # just check if j len == p then all character matched
  # then make j back to 0 so, that we can 
  # check fot other substring
  if j == len(p):
    count += 1
    j = 0

print(count)
