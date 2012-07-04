#!/usr/bin/python

from __future__ import print_function

import sys
import os

MAX_PATH_LENGTH = 40

if len(sys.argv) > 1:
  cwd = sys.argv[1]
  debug = True
else:
  cwd = os.getcwd()
  debug = False

home_path = os.environ['HOME']

if cwd.startswith( home_path ):
  cwd = cwd.replace( home_path, '~' )

ghome_path = '/usr/local/google' + home_path
if cwd.startswith( ghome_path ):
  cwd = cwd.replace( ghome_path, '~' )

path = cwd

if path != '/':
  folders = []
  while True:
    path, folder = os.path.split( path )

    if folder != '':
      folders.append( folder )
    else:
      if path != '':
        folders[-1] = os.path.join( '/', folders[-1] )
      break
  folders.reverse()

  path = os.path.join( *folders )
  if len(folders) > 3 and len(path) > MAX_PATH_LENGTH:
    head = folders[:1]
    tail = folders[-2:]
    body = folders[1:-2]

    largest = 0
    for i in range( 1, len(body) ):
      if len( body[i] ) > len( body[largest] ):
        largest = i
    lbody = body[:largest]
    rbody = body[largest:]

    #loop until path is small enough or it cannot be shrunk any further
    while True:
      path = os.path.join( *(head + lbody + ['..'] + rbody + tail) )

      if len(path) <= MAX_PATH_LENGTH:
        break

      #if both empty, path cannot be shrunk further
      if not lbody and not rbody:
        break

      if not lbody:
        rbody.pop(0)
      elif not rbody:
        lbody.pop(-1)
      elif len(lbody[-1]) < len(rbody[0]):
        rbody.pop(0)
      else:
        lbody.pop(-1)

print( path, end='' )
