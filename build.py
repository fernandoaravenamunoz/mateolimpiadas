import base64
s=open('src.html').read()
logo='data:image/webp;base64,'+base64.b64encode(open('assets/logo.webp','rb').read()).decode()
leon='data:image/webp;base64,'+base64.b64encode(open('assets/leon.webp','rb').read()).decode()
import json,glob,os
imgs={os.path.basename(f)[:-5]:'data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in sorted(glob.glob('assets/p3/*.webp'))}
s=s.replace('__IMAGES__',json.dumps(imgs))
s=s.replace('__PROBLEMAS__',open('problemas.js').read()).replace('__LOGO__',logo).replace('__LEON__',leon)
open('index.html','w').write(s); print(len(s))
