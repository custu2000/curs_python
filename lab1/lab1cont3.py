

def escape_char(char):
 if char=='<':
   return '&lt;'
 elif char=='>':
   return '&gt;'
 elif char=='"':
   return '&quot;'
 elif char=='&':
  return '&amp;'

def html_construct(tip,content):
 list_escape=['<','>','"','&']
 
 for i in list_escape:
   content=content.replace(i,escape_char(i))
 return content

print(html_construct('b','pe ei & copiii mei'))
     




