numbers = ['1','2','3','4','5','6','7','8','9','0']

def find_var(function):
  pass

def find_pi(function):
  d=0
  c=1
  new_fun=""
  for y in function:
    if (c<len(function)):
      check = function[d] + function[c]
      if check == 'pi':
        new_fun+='(math.pi)'
        d+=1
        c+=1
      else:
        new_fun+=function[d]
    d+=1
    c+=1
  if ((function[-2]+function[-1]) != 'pi'):
    new_fun+=function[-1]
  return new_fun

def find_e(function):
  new_fun="";
  for y in function:
    if (y == 'e'):
      new_fun+='(math.e)'
    else:
      new_fun+=y
  return new_fun

def paren_nxt_number(function):
  d=0
  c=1
  new_fun=""
  for y in function:
    if (c<len(function)):
      new_fun+= function[d]
      if (function[d] == ')' and (function[c] in numbers)):
        new_fun += '*'
      elif (function[c] == '(' and (function[d] in numbers)):
        new_fun += '*'
    d+=1
    c+=1
  new_fun += function[-1]
  return new_fun

def paren_nxt_paren(function):
  d=0
  c=1
  new_fun=""
  for y in function:
    if (c<len(function)):
      new_fun+= function[d]
      if (function[d] == ')' and function[c] == '('):
        new_fun += '*'
    d+=1
    c+=1
  new_fun += function[-1]
  return new_fun

def paren_nxt_var(function, var):
  d=0
  c=1
  new_fun=""
  for y in function:
    if (c<len(function)):
      new_fun+= function[d]
      if (function[d] == ')' and (function[c] == var)):
        new_fun += '*'
      elif (function[c] == '(' and (function[d] == var)):
        new_fun += '*'
    d+=1
    c+=1
  new_fun += function[-1]
  return new_fun

def karrot_to_stars(function):
  new_fun = ""
  for y in function:
    if y == '^':
      new_fun+='**'
    else:
      new_fun+=y
  return new_fun

def number_nxt_var(function, var):
  new_fun=""
  c=1
  for y in function:
    if (c<(len(function)) and y in numbers and function[c]==var):
      new_fun+=y
      new_fun+='*'
    else:
      new_fun+=y
    c+=1
  return new_fun

def to_math(function):
  new_fun=""
  fin_fun=""
  var = 'x'
  for x in function:
    if x != ' ':
      new_fun+=x
  fin_fun = karrot_to_stars(new_fun)
  fin_fun = number_nxt_var(fin_fun, var)
  fin_fun = find_pi(fin_fun)
  fin_fun = find_e(fin_fun)
  fin_fun = paren_nxt_number(fin_fun)
  fin_fun = paren_nxt_paren(fin_fun)
  fin_fun = paren_nxt_var(fin_fun, var)
  return fin_fun

def is_in(value, percent, expected):
  percent_up = 1+(percent*.01)
  percent_down = 1-(percent*.01)
  fix_up = expected*percent_up
  fix_down = expected*percent_down
  if (value <= fix_up and value >= fix_down and value >= 0):
    return True
  elif (value >= fix_up and value <= fix_down and value <= 0):
    return True
  else:
    return False

