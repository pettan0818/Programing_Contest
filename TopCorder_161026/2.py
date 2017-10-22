class SortingSubsets(object):
    def getMinimalSize(self, a):
        sorted_list = list(sorted(a))
        return len([i for i,x in zip(a, sorted_list) if i != x])
        
