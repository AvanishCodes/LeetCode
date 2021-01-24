class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> map;
        map.reserve(nums.size());
        for (int i = 0; i < nums.size(); ++i)
        {
            const auto it = map.find(target - nums[i]);
            if (it != end(map))
            {
                return {i, it->second};
            }
            map.emplace(nums[i], i);
        }
        throw invalid_argument("Input has no solution");
    }
};