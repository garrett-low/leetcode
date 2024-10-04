TARGET_SUM = 2020

function report_repair(file)
	local arr = {}
	local handle = assert(io.open(file, "r"))
	local value = handle:read("l")
	while value do
		arr[value] = true
		value = handle:read("l")
	end
	handle:close()

	-- for key, val in pairs(arr) do
	-- 	print(key, val)
	-- end

	-- return arr
	local other_val = -1
	local curr_val = -1
	for key, val in pairs(arr) do
		curr_val = key
		other_val = TARGET_SUM - curr_val
		if arr[other_val] then
			break
		end
	end

	if other_val == -1 then
		print("P1: Not found!")
	else
		local p1_solution = curr_val * other_val
		print("P1: " .. curr_val .. " * " .. other_val .. " = " .. p1_solution)
	end
end

report_repair("sample.txt")
report_repair("input.txt")
