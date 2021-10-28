#script to generate projects file
import json
import os
projectlist=os.listdir('C:/Users/antonyalbertraj/Desktop/website_antony/website_antony/python_scripts/data/')
print("projectlist",projectlist)

basedir="C:/Users/antonyalbertraj/Desktop/website_antony/website_antony/python_scripts/data/"


def values(projectname):
    filename=basedir+projectname
    print("filename",filename)
    f=open(filename)
    lines=json.load(f)
    project_name=lines['name']
    project_desc=lines['desc']
    return project_name,project_desc

f1=open('sample.html','w')
f1.writelines('<html>\n')
f1.writelines('<title>Projects\n')
f1.writelines('</title>\n')

f1.writelines('<table id="research" class="table" style="table-layout: fixed;width=100%">')


i=0
while i<4:
    f1.writelines("<tr>\n")

    project_name1,project_desc1=values(projectlist[i])
    project_name2,project_desc2=values(projectlist[i+1])
    project_name3,project_desc3=values(projectlist[i+2])
    project_name4,project_desc4=values(projectlist[i+3])

    f1.writelines("""<td style="text-align:center"> <figure><a href="""+str(projectlist[i].strip('.json'))+""".html> <img src="""+str(projectlist[i].strip('.json'))+""".jpg width="300" height="300"></a><figcaption><b>"""+str(project_name1)+"""<br></b>"""+str(project_desc1)+"""</figcaption></figure> </td>\n""")
    f1.writelines("""<td style="text-align:center"> <figure><a href="""+str(projectlist[i+1].strip('.json'))+""".html> <img src="""+str(projectlist[i+1].strip('.json'))+""".jpg width="300" height="300"></a><figcaption><b>"""+str(project_name2)+"""<br></b>"""+str(project_desc2)+"""</figcaption></figure> </td>\n""")
    f1.writelines("""<td style="text-align:center"> <figure><a href="""+str(projectlist[i+1].strip('.json'))+""".html> <img src="""+str(projectlist[i+2].strip('.json'))+""".jpg width="300" height="300"></a><figcaption><b>"""+str(project_name3)+"""<br></b>"""+str(project_desc3)+"""</figcaption></figure> </td>\n""")
    f1.writelines("""<td style="text-align:center"> <figure><a href="""+str(projectlist[i+1].strip('.json'))+""".html> <img src="""+str(projectlist[i+3].strip('.json'))+""".jpg width="300" height="300"></a><figcaption><b>"""+str(project_name4)+"""<br></b>"""+str(project_desc4)+"""</figcaption></figure> </td>\n""")
    
#    f1.writelines("""<td align="justify" valign="top" style="word-wrap: break-word;width:800px"> <b><h3>"""+str(project_desc)+"""</h3></b>\n""")
    f1.writelines("</td>\n")
    f1.writelines("</tr>\n")
    i+=4 
##	</td>
## </tr>
f1.writelines('</table>\n')
f1.writelines('</html>\n')
f1.close()

