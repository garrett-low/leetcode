function trebuchet(file)
    local arr = {}
    local handle = assert(io.open(file, "r"))
    local value = handle:read("l")
    while value do
        table.insert(arr, value)
        value = handle:read("l")
    end
    handle:close()
    
    -- for key, val in ipairs(arr) do print(key, val) end
    
    return arr
end

function part_one(file)
    local vals = {}
    local input_lines = trebuchet(file)
    for i = 1, #input_lines, 1 do
        local input_line = input_lines[i]
        local first_dig = nil
        local last_dig = nil
        for j = 1, #input_line, 1 do
            local char_curr = input_line:sub(j, j)
            -- print(char_curr)
            -- local char_type = type(char_curr)
            if tonumber(char_curr) then
                first_dig = char_curr
                -- print(char_curr)
                break
            end
        end
        for j = #input_line, 1, -1 do
            local char_curr = input_line:sub(j, j)
            if tonumber(char_curr) then
                last_dig = char_curr
                break
            end
        end
        table.insert(vals, tostring(first_dig) .. tostring(last_dig))
    end
    
    for key, val in ipairs(vals) do print(key, val) end
    local sum = 0
    for key, val in ipairs(vals) do
        sum = sum + tonumber(val)
    end
    
    print("P1: " .. sum)
    return sum
end

trebuchet("sample.txt")
part_one("sample.txt")