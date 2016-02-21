import java.time.Instant;
import java.util.NoSuchElementException;
import java.util.concurrent.BlockingDeque;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.LinkedBlockingDeque;

/**
 * @author Amit Saha
 * 
 */

/* Message on the queue */
class Message {
	private String body;
	private long consumedTime = 0;

	String getBody() {
		return this.body;
	}

	void setConsumedTime(long epoch) {
		this.consumedTime = epoch;
	}

	long getConsumedTime() {
		return this.consumedTime;
	}

	Message(String body) {
		this.body = body;
	}
}

/* Producer class */
class Producer implements Runnable {

	private final BlockingDeque<Message> queue;
	private int num;

	Producer(int num, BlockingDeque<Message> q) {
		this.num = num;
		this.queue = q;
	}

	public void run() {

		try {
			while (true) {
				this.queue.putLast(produce());
			}
		} catch (InterruptedException ex) {
			System.out.println("Exception");
		}
	}

	Message produce() {
		System.out.println("Producer: " + this.num);
		return new Message("task");
	}
}

/* Consumer class */
class Consumer implements Runnable {
	private final BlockingDeque<Message> queue;
	private ConcurrentLinkedQueue<Message> to_consumer;
	private int num;

	Consumer(int num, BlockingDeque<Message> q, ConcurrentLinkedQueue<Message> q1) {
		this.num = num;
		this.queue = q;
		this.to_consumer = q1;
	}

	public void run() {
		while (true) {
			try {
				Message msg = this.queue.removeFirst();
				if (msg != null) {
					msg.setConsumedTime(Instant.now().getEpochSecond());
					this.to_consumer.add(msg);
					consume(msg);
				}
			} catch (NoSuchElementException e) {
				System.out.println(e.getMessage());

			}

		}
	}

	void consume(Message m) {
		System.out.println("Consumer: " + this.num);
		// Remove the message
		this.to_consumer.remove(m);
	}
}

// Go over all the messages currently present in to_consumer queue
// and check if they have expired, if yes, put them back to
class ConsumedMessageChecker implements Runnable {

	private ConcurrentLinkedQueue<Message> to_consumer;
	private BlockingDeque<Message> queue;

	ConsumedMessageChecker(ConcurrentLinkedQueue<Message> q1, BlockingDeque<Message> q2) {
		this.to_consumer = q1;
		this.queue = q2;
	}

	public void run() {
		while (true) {
			Message msg = this.to_consumer.peek();
			if (msg != null) {
				if ((Instant.now().getEpochSecond() - msg.getConsumedTime()) > 60) {
					// put it back to the queue to be consumed
					this.queue.addFirst(msg);
					// Remove the msg from to_consumer
					this.to_consumer.remove(msg);
				}
			}

		}
	}

}

/* Driver */
public class Main {
	public static void main(String[] args) {
		// Main message queue
		BlockingDeque<Message> q = new LinkedBlockingDeque<Message>();
		// Queue for queuing the messages sent to the consumer
		ConcurrentLinkedQueue<Message> toConsumer = new ConcurrentLinkedQueue<Message>();

		// Create the producers
		Producer p1 = new Producer(1, q);
		Producer p2 = new Producer(2, q);

		// Create the consumers
		Consumer c1 = new Consumer(1, q, toConsumer);
		Consumer c2 = new Consumer(2, q, toConsumer);

		// Start the producers and consumers
		new Thread(p1).start();
		new Thread(c1).start();

		// new Thread(p2).start();
		new Thread(c2).start();
		new Thread(p2).start();

		// Cleaning thread
		ConsumedMessageChecker checker = new ConsumedMessageChecker(toConsumer, q);
		new Thread(checker).start();
	}
}
