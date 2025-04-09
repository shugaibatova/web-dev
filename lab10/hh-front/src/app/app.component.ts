// src/app/app.component.ts
import { Component } from '@angular/core';
import { CompanyService } from './services/company.service';
import { Company } from './models/company';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { VacancyListComponent } from './components/vacancy-list/vacancy-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, VacancyListComponent, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  companies: Company[] = [];
  selectedCompanyId: number | null = null;

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((data) => {
      this.companies = data;
    });
  }

  onSelectCompany(companyId: number): void {
    this.selectedCompanyId = companyId;
  }
}
