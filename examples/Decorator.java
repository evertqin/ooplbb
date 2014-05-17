// --------------
// Decorator.java
// --------------

// http://en.wikipedia.org/wiki/Decorator_pattern

interface PizzaInterface {
	int getCost ();}

class Pizza implements PizzaInterface {
    public final int getCost () {
        return 7;}

	public final String toString () {
		return "Pizza";}}

abstract class AbstractPizzaDecorator implements PizzaInterface {
    protected PizzaInterface _p;

    public AbstractPizzaDecorator (PizzaInterface p) {
        _p = p;}}

class CheesePizzaDecorator extends AbstractPizzaDecorator {
	public CheesePizzaDecorator (PizzaInterface p) {
		super(p);}

	public final int getCost () {
		return _p.getCost() + 1;}

	@Override
	public final String toString () {
		return "Cheese " + _p.toString();}}

class SausagePizzaDecorator extends AbstractPizzaDecorator {
	public SausagePizzaDecorator (PizzaInterface p) {
		super(p);}

	public final int getCost () {
		return _p.getCost() + 2;}

	@Override
	public final String toString () {
		return "Sausage " + _p.toString();}}

final class Decorator {
    public static void main (String[] args) {
        System.out.println("Decorator.java");

		{
        PizzaInterface p = new Pizza();
        assert p.getCost() == 7;
        assert p.toString().equals("Pizza");
		}

		{
        PizzaInterface p = new CheesePizzaDecorator(new Pizza());
        assert p.getCost() == 8;
        assert p.toString().equals("Cheese Pizza");
		}

		{
        PizzaInterface p = new CheesePizzaDecorator(new SausagePizzaDecorator(new Pizza()));
        assert p.getCost() == 10;
        assert p.toString().equals("Cheese Sausage Pizza");
		}

		{
        PizzaInterface p = new CheesePizzaDecorator(new SausagePizzaDecorator(new CheesePizzaDecorator(new Pizza())));
        assert p.getCost() == 11;
        assert p.toString().equals("Cheese Sausage Cheese Pizza");
		}

        System.out.println("Done.");}}
