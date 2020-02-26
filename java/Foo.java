

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

class Foo_1 {

  private AtomicInteger firstJobDone = new AtomicInteger(0);
  private AtomicInteger secondJobDone = new AtomicInteger(0);

  public Foo_1() {}

  public void first(Runnable printFirst) throws InterruptedException {
    // printFirst.run() outputs "first".
    printFirst.run();
    // mark the first job as done, by increasing its count.
    firstJobDone.incrementAndGet();
  }

  public void second(Runnable printSecond) throws InterruptedException {
    while (firstJobDone.get() != 1) {
      // waiting for the first job to be done.
    }
    // printSecond.run() outputs "second".
    printSecond.run();
    // mark the second as done, by increasing its count.
    secondJobDone.incrementAndGet();
  }

  public void third(Runnable printThird) throws InterruptedException {
    while (secondJobDone.get() != 1) {
      // waiting for the second job to be done.
    }
    // printThird.run() outputs "third".
    printThird.run();
  }
}

class Foo_2 {

  Semaphore run2, run3;

  public Foo_2() {
    run2 = new Semaphore(0);
    run3 = new Semaphore(0);
  }

  Runnable printFirst =
      new Runnable() {
        public void run() {
          System.out.print("first");
          run2.release();
        }
      };

  Runnable printSecond =
      new Runnable() {
        public void run() {
          try {
            run2.acquire();
          } catch (InterruptedException e) {
            System.out.println("Error");
          }
          System.out.print("second");
          run3.release();
        }
      };

  Runnable printThird =
      new Runnable() {
        public void run() {
          try {
            run3.acquire();
          } catch (InterruptedException e) {
            System.out.println("Error");
          }
          System.out.print("third");
        }
      };
  

  public static void main(String[] args) {
    Foo_2 bar = new Foo_2();

    Thread one = new Thread(bar.printFirst);
    Thread two = new Thread(bar.printSecond);
    Thread three = new Thread(bar.printThird);

    one.start();
    two.start();
    three.start();
  }
  
}
