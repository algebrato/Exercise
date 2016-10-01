import java.awt.*;
import java.awt.event.*;

public class GraphSampl extends Frame implements ActionListener{
	private Label lblCount;
	private TextField tftCount;
	private Button btnCount;
	private int count = 0;


	public GraphSampl(){
		setLayout(new FlowLayout());
		lblCount = new Label("Counter");
		add(lblCount);

		tftCount = new TextField("0",10);
		tftCount.setEditable(false);
		add(tftCount);

		btnCount = new Button("Count");
		add(btnCount);
		btnCount.addActionListener(this);

		setTitle("AWT Counter");
		setSize(250,100);

		setVisible(true);
	}

	public static void main(String[] args){
		new GraphSampl();
	}

	@Override
	public void actionPerformed(ActionEvent evt){
		++count;
		tftCount.setText(count + "");
	}
}
