# detect the Ctrl+C from the keyboard
  
  try: 
      do_some_func()
  except KeyboardInterrupt:
      print "User Press Ctrl+C,Exit"
  except EOFError:
      print "User Press Ctrl+D,Exit"