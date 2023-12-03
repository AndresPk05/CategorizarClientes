import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { GroupCliente } from '../groupClient';
import Chart from 'chart.js/auto';
import { ResultGrafic } from '../resultGrafic';
@Component({
  selector: 'app-grafic',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './grafic.component.html',
  styleUrl: './grafic.component.css'
})
export class GraficComponent {
  @Input() clients!: GroupCliente;
  @Input() labels!: Number[];

  chart: any;
  dataGrafic: any = {};
  resultGrafic: ResultGrafic[] = [];

  constructor() {
   }

   ngOnInit(): void {
    this.makeDataGrafic();
  }

  makeDataGrafic(): void{
    let datasets: any[] = [];
    let colors: string[] = ['red', 'blue', 'green', 'purple', 'orange'];
    let indexColor = 0;
    for(let key in this.labels){
      let data: any[] = [];
      let resultGrafic: ResultGrafic = {
        label: 'Grupo Numero ' + (Number(key) + 1),
        countUsers: this.clients[key].length
      };

      this.clients[key].forEach((item: any) => {
        data.push({x: item.x, y: item.y});
      });
      datasets.push({
        label: 'Grupo Numero ' + (Number(key) + 1),
        data: data,
        backgroundColor: colors[indexColor],
        borderColor: colors[indexColor],
        borderWidth: 1
      });
      this.resultGrafic.push(resultGrafic);
      indexColor++;
    }
    this.dataGrafic = {
      datasets: datasets
    };

    this.chart = new Chart('MyChart', {
      type: 'scatter',
      data: this.dataGrafic,
      options: {
        scales: {
          x: {
            type: 'linear',
            position: 'bottom'
          }
        }
      }
    });
  }
}
