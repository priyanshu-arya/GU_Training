package Day_4.Sliding_Window.code.Solution_6;
import java.util.*;

class sol {
    private PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> large = new PriorityQueue<>();
    private Map<Integer, Integer> delayed = new HashMap<>();
    private int k, smallSize = 0, largeSize = 0;

    public double[] medianSlidingWindow(int[] nums, int k) {
        this.k = k;
        double[] res = new double[nums.length - k + 1];
        for (int i = 0; i < k; ++i) insert(nums[i]);
        res[0] = getMedian();
        for (int i = k; i < nums.length; ++i) {
            insert(nums[i]);
            erase(nums[i - k]);
            res[i - k + 1] = getMedian();
        }
        return res;
    }

    private void insert(int num) {
        if (small.isEmpty() || num <= small.peek()) {
            small.offer(num);
            smallSize++;
        } else {
            large.offer(num);
            largeSize++;
        }
        balance();
    }

    private void erase(int num) {
        delayed.put(num, delayed.getOrDefault(num, 0) + 1);
        if (num <= small.peek()) {
            smallSize--;
            if (num == small.peek()) prune(small);
        } else {
            largeSize--;
            if (num == large.peek()) prune(large);
        }
        balance();
    }

    private void balance() {
        if (smallSize > largeSize + 1) {
            large.offer(small.poll());
            smallSize--;
            largeSize++;
            prune(small);
        } else if (smallSize < largeSize) {
            small.offer(large.poll());
            largeSize--;
            smallSize++;
            prune(large);
        }
    }

    private void prune(PriorityQueue<Integer> heap) {
        while (!heap.isEmpty()) {
            int num = heap.peek();
            if (delayed.getOrDefault(num, 0) > 0) {
                delayed.put(num, delayed.get(num) - 1);
                heap.poll();
            } else break;
        }
    }

    private double getMedian() {
        return k % 2 == 1 ? (double) small.peek()
                : ((double) small.peek() + large.peek()) / 2;
    }
}
