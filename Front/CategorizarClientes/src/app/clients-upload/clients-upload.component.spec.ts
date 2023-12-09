import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientsUploadComponent } from './clients-upload.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from "@angular/router/testing";

describe('ClientsUploadComponent', () => {
  let component: ClientsUploadComponent;
  let fixture: ComponentFixture<ClientsUploadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClientsUploadComponent, HttpClientTestingModule, RouterTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ClientsUploadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
