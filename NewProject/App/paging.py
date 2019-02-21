from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# 分页模块
def paging(page,obj,perpages):
	# 查询数据库中所有数据
	# music_list = MusicList.objects.all()
	# 创建paginator对象 需两个参数 参数1为要被分页的对象，参数2为每页显示数量
	print(page, obj, perpages)
	paginator = Paginator(obj, perpages)
	try:
		# 获取pages对象传递给页面
		pages = paginator.page(page)
	# 	当传递页数的参数不为整数时，页码默认为1（一般在刷新页面时）
	except PageNotAnInteger:
		pages = paginator.page(1)
	# 	当页面为空时，将显示最后一页内容
	except EmptyPage:
		pages = paginator.page(paginator.num_pages)
	return pages