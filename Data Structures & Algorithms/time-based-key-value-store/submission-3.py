class TimeMap:

    def __init__(self):
        self.data = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key]=[(timestamp,value)]
        else:
            self.data[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ("")
        arr=self.data[key]
        ans=-1

        left=0
        right=len(arr)-1
        while left<=right:

            mid=(right+left)//2 
            if arr[mid][0]<=timestamp:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        if ans==-1:
            return ""
        else:
            return (arr[ans][1])



