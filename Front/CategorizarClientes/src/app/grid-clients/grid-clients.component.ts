import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Client } from '../client';
@Component({
  selector: 'app-grid-clients',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './grid-clients.component.html',
  styleUrl: './grid-clients.component.css'
})
export class GridClientsComponent {
  @Input() clients!: Client[];
}
