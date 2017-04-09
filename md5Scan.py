import os
import sys
import hashlib
import glob

  # THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED WARRANTIES,
  # INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
  # FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL JCRAFT,
  # INC. OR ANY CONTRIBUTORS TO THIS SOFTWARE BE LIABLE FOR ANY DIRECT, INDIRECT,
  # INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
  # LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
  # OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  # LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  # NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
  # EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


filepath =''
checksumlist = []

def csv(fname):
    f = open('checksum.csv','w')
    for list in (fname):
         f.write(list+'\n')
    f.close

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def mdexplore(walk_dir):
    for filename in glob.iglob(walk_dir,recursive=True):
        if os.path.isfile(filename):
            print(filename+","+md5(filename))
            value = md5(filename)
            checksumlist.append(filename+','+value)
    csv(checksumlist)

for i, arg in enumerate(sys.argv):
    if arg=='-f':
        filepath=sys.argv[i+1]
if filepath=='':
    print('use -f to define your file path')
    sys.exit(0)

print('Searching '+filepath)
searchpath = filepath+'/**'
mdexplore(searchpath)

