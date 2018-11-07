
print("made it to common setup")
function table_dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. table_dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

function keys( x)
  local keyset={}
  local n=0

  for k,v in pairs(x) do
       n=n+1
       keyset[n]=k
  end
  return keyset
  end
  
  