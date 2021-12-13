/// <reference types="cypress" />

// Welcome to Cypress!
//
// This spec file contains a variety of sample tests
// for a todo list app that are designed to demonstrate
// the power of writing tests in Cypress.
//
// To learn more about how Cypress works and
// what makes it such an awesome testing tool,
// please read our getting started guide:
// https://on.cypress.io/introduction-to-cypress

describe('Home Page', () => {
  beforeEach(() => {
    cy.visit('https://kigest.herokuapp.com')
  })
  it('displays two items by default', () => {
    cy.get('.form-floating').should('have.length', 2)
    cy.get('.form-floating input').eq(0).invoke('attr','placeholder').should('contain','Username')
    cy.get('.form-floating input').eq(0).type('stevetestt')
    cy.get('.form-floating input').should('have.value', 'stevetestt')
    cy.get('.form-floating input').eq(1).invoke('attr','placeholder').should('contain', 'Password')
    cy.get('.form-floating input').eq(1).type('Test1234*')
    cy.get('.form-floating input').eq(1).type('{enter}')
  })
})

describe('Employee Tasks', () => {
  beforeEach(() => {
    cy.visit('https://kigest.herokuapp.com')
    cy.get('.form-floating input').eq(0).type('stevetestt')
    cy.get('.form-floating input').eq(1).type('Test1234*')
    cy.get('.form-floating input').eq(1).type('{enter}')
  })
  it('Tasks Test', () => {
    cy.contains('Tasks').click()
    cy.url().should('include','/tasks')
  })

  it('Schedule Test', () => {
    cy.contains('Scheduling').click()
    cy.url().should('include','/schedule')
  })

  it('Payroll Test', () => {
    cy.contains('Payroll').click()
    cy.url().should('include','/payroll')
    cy.get('.form-control').should('have.length',2)
    cy.get('.btn-primary').should('have.length',1)
    cy.get('.form-control').eq(0).invoke('attr','name').should('contain','pay_period_start')
    cy.get('.form-control').eq(0).type('2021-11-01')
    cy.get('.form-control').eq(1).invoke('attr','name').should('contain','pay_period_end')
    cy.get('.form-control').eq(1).type('2021-12-01')
    cy.contains('Get Paystub').click()
  })

  it('Dashboard Test', () => {
    cy.contains('Dashboard').click()
    cy.url().should('include','/')
  })

  it('Kigest Test', () => {
    cy.contains('Kigest').click()
    cy.url().should('include','/')
  })

  it('Profile Test', () => {
    cy.contains('Stevetestt').click()
    cy.url().should('include','/profile/stevetestt')
  })

  it('Logout Test', () => {
    cy.contains('Logout').click()
    cy.url().should('include','/profile/login')
  })
})

describe('ManagerTasks', () => {
  beforeEach(() => {
    cy.visit('https://kigest.herokuapp.com')
    cy.get('.form-floating input').eq(0).type('Geooh')
    cy.get('.form-floating input').eq(1).type('project123')
    cy.get('.form-floating input').eq(1).type('{enter}')
  })

  it('managerTasks', () => {
    cy.contains('Tasks').click()
    cy.url().should('include','/tasks')
    cy.contains('Assign a New Task').click()
    cy.url().should('include','/tasks/createtask')
    cy.get('.form-control').should('have.length',3)
    cy.get('[type="checkbox"]').should('have.length',10)
    cy.get('.form-control').eq(0).type('Task Test')
    cy.get('.form-control').eq(1).type('Testing the creation of a new task')
    cy.get('[type="checkbox"]').eq(7).check({force:true})
    cy.get('.form-control').eq(2).type('2021-12-20')
    cy.contains('Create this task').click()
  })

  it('managerSchedule', () => {
    cy.contains('Scheduling').click()
    cy.url().should('include','/schedule')
    cy.contains('View Time Off Requests').click()
    cy.url().should('include','/schedule/timeoff')
    cy.contains('Request Time Off').click()
    cy.url().should('include','/schedule/newtimeoff')
    cy.get('.form-control').should('have.length',4)
    cy.get('.form-control').eq(0).select('Stevetestt')
    cy.get('.form-control').eq(1).type('Sick')
    cy.get('.form-control').eq(2).type('2021-12-09')
    cy.get('.form-control').eq(3).type('2021-12-11')
    cy.contains('Submit Request').click()
  })

  it('managerPayroll', () => {
    cy.contains('Payroll').click()
    cy.url().should('include','/payroll')
    cy.get('.form-control').should('have.length',3)
    cy.get('.form-control').eq(0).select('Stevetestt')
    cy.get('.form-control').eq(1).type('2021-10-01')
    cy.get('.form-control').eq(2).type('2021-12-01')
    cy.contains('Get Paystub').click()
  })

  it('Logout Test', () => {
    cy.contains('Logout').click()
    cy.url().should('include','/profile/login')
  })  
})
/*
https://glebbahmutov.com/blog/cy-metaprogramming/
*/
