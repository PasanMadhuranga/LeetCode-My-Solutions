class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // Initialize starting position, current oil in the tank, and total oil
        // difference
        int startPos = 0;
        int currOil = 0;
        int totOil = 0;
        int l = gas.length;

        // Loop through each gas station
        for (int i = 0; i < l; i++) {
            // Update the total oil difference after considering this station
            totOil += gas[i] - cost[i];
            // Update the current oil in the tank after this station
            currOil += gas[i] - cost[i];

            // If current oil in the tank is less than 0, the car can't reach the next
            // station
            if (currOil < 0) {
                // Reset the current oil to 0 as we select a new starting position
                currOil = 0;
                // Set the new starting position to the next station
                startPos = i + 1;
            }
        }
        // If the total oil difference is negative, it's impossible to complete the
        // circuit
        // Otherwise, return the starting position
        return totOil < 0 ? -1 : startPos;
    }
}
