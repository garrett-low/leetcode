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

function report_repair_p2(file)
	local arr = {}
	local handle = assert(io.open(file, "r"))
	local value = handle:read("l")
	while value do
		arr[tonumber(value)] = true
		value = handle:read("l")
	end
	handle:close()

	local first_remainder
	local second_remainder
	local is_found
	local p2_sol
	for key, _ in pairs(arr) do
		first_remainder = TARGET_SUM - key

		for second_key, _ in pairs(arr) do
			if key == second_key then
				goto continue
			end

			second_remainder = first_remainder - second_key
			if second_remainder < 0 then
				goto continue
			end
			-- Forgot to convert the input
			if arr[second_remainder] then
				is_found = true
				p2_sol = key * second_key * second_remainder
				break
			end

			::continue::
		end

		if is_found then
			break
		end
	end

	if is_found then
		print("P2: " .. p2_sol)
	else
		print("P2 not found!")
	end
end

report_repair_p2("sample.txt")
report_repair_p2("input.txt")
