import simulator
import visualizer
import time

def main():
    print("Starting simulation...")
    start_time = time.time()
    
    # 1. starting simulation
    list_of_results = simulator.run_full_simulation() 
    
    # 2. calculating time
    print(f"calculation is over. Total time: {time.time() - start_time:.2f} second")
    
    # 3. sketching graph
    print("Sketching the graph...")
    visualizer.plot_results(list_of_results)
    print("The graph is saved on the local folder!")

if __name__ == "__main__":
    main()