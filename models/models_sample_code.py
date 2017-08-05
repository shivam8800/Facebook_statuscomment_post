def all_comments(main_id):
	status = Status.objects.get(id=main_id)
	all_comments = Comment.objects.all()
	answer =all_comments.filter(status_id=main_id)
	return answer

def all_comments(main_id):
	status = Status.objects.get(id=main_id)
	ans = status.comment_set.all()
	return ans


# SECOND QUESTION

list =[]
all_status = Status.objects.all()
dict ={}
for i in all_status:
	dict['status'] = i.status_text
	comments = i.comment_set.all()
	dict['comments'] = comments
	list.append(dict)
	dict ={}		
print list