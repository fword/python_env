import sys,os
import traceback
class Objimage:
	def __init__(self,objurl="",furl=[],id="",txtlist=[]):
		self.objurl=objurl
		self.id=id
		self.furl=furl
		self.txtlist=txtlist
def gen_html(obj,candi):
	if not isinstance(candi,list):
		return ""
	if isinstance(candi[0],list):
		rows=len(candi)
		cols=len(candi[0])
	else:
		rows=1
		cols=len(candi[0])

	tmp_line="<div class=\"img_keyword\"><p>[ index ]:%s &nbsp;</p>\n" %(obj.id)
	for furlone in obj.furl:
		tmp_line += "<p><a href=\"%s\">%s&nbsp</a></p>\n" % (furlone['url'],furlone['name'])
	for txtone in obj.txtlist:
		tmp_line += "<p>%s:%s</p>\n" % (txtone['name'],txtone['content'])
	tmp_line += "<p><img src=%s height=200></p></div><br><br>\n" % (obj.objurl)
	tmp_line += '<div><table>'
	for rowitem in candi:
		tmp_line += '<tr>'
		for colsitem in rowitem:
			tmp_line += '<td width="33%"><div>'
			item = colsitem
			if 1 == 1:
				if item.id:
					tmp_line += '<div><p>%s</p></div>' %(item.id)
				tmp_line += '<table><tr>'
				if item.objurl:
					tmp_line += '<td><div><img src="%s"></div></td>' %(item.objurl)
				tmp_line += '</tr></table>'
				if len(item.txtlist):
					for txtone in item.txtlist:
						tmp_line += "<p>%s:%s</p>\n" % (txtone['name'],txtone['content'])
				if len(item.furl):
					for furlone in item.furl:
						tmp_line += "<p><a href=\"%s\">%s&nbsp</a></p>\n" % (furlone['url'],furlone['name'])
			tmp_line += '</div></td>'
		tmp_line += '</tr>'
	tmp_line += '</table></div><br><br>'
	return tmp_line
