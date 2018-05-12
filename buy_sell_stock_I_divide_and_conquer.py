
def find_best_price(ip_arr):
	if len(ip_arr)<=1:
		return 0
	def profit_min_idx_max_idx(arr, min_idx, max_idx):
		if min_idx==max_idx:
			return(0,arr[min_idx],arr[max_idx])
		mid = min_idx+ (max_idx-min_idx)/2
		l_profit, l_min, l_max = profit_min_idx_max_idx(arr,min_idx,mid)
		r_profit, r_min, r_max = profit_min_idx_max_idx(arr,mid+1, max_idx)
		profit = max(l_profit,r_profit,r_max-l_min)
		return (profit, min(l_min,r_min), max(l_max,r_max))
	best_profit,_,_ = profit_min_idx_max_idx(ip_arr,0,len(ip_arr)-1)
	return best_profit


def main():
	ip_arr = [7,1,5,3,6,4]
	print find_best_price(ip_arr)

if __name__=="__main__":
	main()