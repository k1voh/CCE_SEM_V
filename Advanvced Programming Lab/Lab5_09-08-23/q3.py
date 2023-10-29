#unique subsets of an array using a class

class subsets:
    def ssets(self, arr):
       return self.subSets([], sorted(arr))
        
    def subSets(self, curr, arr):
        if arr:
            return self.subSets(curr, arr[1:]) + self.subSets(curr + [arr[0]], arr[1:])
        return [curr]
    
print(subsets().ssets([4,5,6]))