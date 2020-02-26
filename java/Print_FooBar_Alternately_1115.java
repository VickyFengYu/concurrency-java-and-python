

import java.util.concurrent.Semaphore;

public class Print_FooBar_Alternately_1115 {
  private int n;
  Semaphore bar_semaphore = new Semaphore(0);
  Semaphore foo_semaphore = new Semaphore(1);

  public Print_FooBar_Alternately_1115(int n) {
    this.n = n;
  }

  public void foo(Runnable printFoo) throws InterruptedException {

    for (int i = 0; i < n; i++) {
      foo_semaphore.acquire();

      printFoo.run();

      bar_semaphore.release();
    }
  }

  public void bar(Runnable printBar) throws InterruptedException {

    for (int i = 0; i < n; i++) {

      bar_semaphore.acquire();

      printBar.run();

      foo_semaphore.release();
    }
  }
  
}
