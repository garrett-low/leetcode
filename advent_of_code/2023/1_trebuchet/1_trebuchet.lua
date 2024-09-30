function trebuchet(file)
    local arr = {}
    local handle = assert(io.open(file, "r"))
    local value = handle:read("l")
    while value do
        table.insert(arr, value)
        value = handle:read("l")
    end
    handle:close()
    
    for key, val in ipairs(arr) do print(key, val) end
    
    return arr
end

trebuchet("input.txt")