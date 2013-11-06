import java.util.ArrayList;


public class CarSpawn extends Spawn {
	public ArrayList<Car> cars = new ArrayList<Car>();
	public int creating = 0;
	public int cCount = 0;
	public CarSpawn(Map map,int x,int y,boolean left){
		super(map,x,y,left);
	}
	public void run(){
		cCount++;
		if(left||cCount%2==0){
		counter++;
		
		
		for(int i=0;i<cars.size();i++){
			if(cars.get(i).run(left)){
				map.grid[cars.get(i).posY][cars.get(i).posX].contents.remove(cars.get(i));
				cars.remove(cars.get(i));
				i--;
			}
		
		}
		
		if((counter%10==0)||creating%2!=0){
			Car c = new Car(map, x, y);
			map.grid[y][x].contents.add(c);
			cars.add(c);
			creating++;
			if(creating%2==0){
				this.resetCounter();
			}
		}
		}
		
	}
}
