from __future__ import annotations
from typing import Dict, List, Type
class FuzzySet():
    
    def __init__(self, d: Dict):
        self.fset: Dict = d.copy()
        
    def union(self, set2: FuzzySet) -> FuzzySet:
        d = self.fset.copy()
        for key, val in set2.fset.items():
            if key in d.keys():
                d[key] = max(d[key], val)
            else:
                d[key] = val
        
        return FuzzySet(d)
        
    def intersection(self, set2: FuzzySet) -> FuzzySet:
        d= {}
        for key, val in self.fset.items():
            if key in set2.fset.keys():
                d[key] = min(val, set2.fset[key])
                
        return FuzzySet(d)

    def compliment(self) -> FuzzySet:
        d = {}
        for key, value in self.fset.items():
            d[key] = round(1-value, 2)
            
        return FuzzySet(d)

    def difference(self, set2: FuzzySet) -> FuzzySet:
        d = {}
        for key, val in self.fset.items():
            if key in set2.fset.keys():
                d[key] = round(min(val, 1-set2.fset[key]), 2)
                
        return FuzzySet(d)

    def __str__(self) -> str:
        pr = "{"
        for key, val in self.fset.items():
            pr += str(key) + ": " + str(val) + ", "
        
        pr += "}"
        return pr

    def cartesian_product(self, set2: FuzzySet) -> List:
      cp = []
      for i in self.fset:
        temp = []
        for j in set2.fset:
           temp.append(min(self.fset[i], set2.fset[j]))
        cp.append(temp)
        
      return cp

#demorgan 
    
def de_morgans(f1: FuzzySet, f2:FuzzySet):

    print("\nDe Morgan's 1st law: ")

    exp1 = f1.intersection(f2).compliment()
    exp2 = f1.compliment().union(f2.compliment()) 
    print(exp1)
    print(exp2)

    if exp1.fset == exp2.fset:
        print("--> Satisfies")
    else:
        print("--> Does not satisy")
    
    print("\nDe Morgan's 2nd law: ")

    exp1 = f1.union(f2).compliment()
    exp2 = f1.compliment().intersection(f2.compliment()) 
    print(exp1)
    print(exp2)

    if exp1.fset == exp2.fset:
        print("--> Satisfies")
    else:
        print("--> Does not satisy")

#mini max 
def min_max_composition(R: List, S: List):
  RoS = []
  S = [list(i) for i in zip(*S)]
  for i in R:
    t = []
    for j in S:
      c = 0
      for t1, t2 in zip(i,j):
        c = max(c, min(t1, t2))
      t.append(c)
      # print(i, " | ", j, "-->", t)
    RoS.append(t)
  
  return RoS

#driver code
def fuzzy_demo():
    a = {2:1, 3:0.4, 1:0.6, 4:0.2}
    b = {2:0, 3:0.2, 1:0.2, 4:0.8}
    
    f1 = FuzzySet(a)
    f2 = FuzzySet(b)

    print("f1: \t", f1)
    print("f2: \t", f2)
    print("f1 U f2: ", f1.union(f2))
    print("f1 ^ f2: ", f1.intersection(f2))
    print("~f1: \t", f1.compliment())
    print("f1 - f2: ", f1.difference(f2))
    de_morgans(f1, f2)

    a = {2:1, 3:0.4, 1:0.6, 4:0.2}
    b = {5:0, 7:0.2, 6:0.2, 8:0.8}
    c = {2:0.5, 3:0.6, 1:0.1, 4:0.9}

    fa = FuzzySet(a)
    fb = FuzzySet(b)
    fc = FuzzySet(c)

    Rel_R = fa.cartesian_product(fb)
    Rel_S = fa.cartesian_product(fc)

    print("R = A X B: ", Rel_R)
    print("S = A X C: ", Rel_S)

    print("\nMin-Max Composition (R & S):", *min_max_composition(Rel_R, Rel_S), sep="\n")

fuzzy_demo()