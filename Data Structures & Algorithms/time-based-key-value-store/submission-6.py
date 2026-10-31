class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ""
        lst_to_search = self.time_map[key]
        l = 0
        r = len(lst_to_search)-1
        closest_to_lower = 0
        closest_to_lower_index = -1
        while l<=r:
            mid = l + (r-l)//2
            if lst_to_search[mid][1] == timestamp:
                return lst_to_search[mid][0]
            elif lst_to_search[mid][1] > timestamp:
                r = mid-1
            else:
                l = mid+1
                closest_to_lower = max(closest_to_lower, lst_to_search[mid][1])
                closest_to_lower_index = max(closest_to_lower_index, mid)
        
        if closest_to_lower_index != -1:
            return lst_to_search[closest_to_lower_index][0]
        else:
            return ""

        
        
        




        
