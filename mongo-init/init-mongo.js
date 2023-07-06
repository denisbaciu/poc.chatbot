db.auth('root', 'example')
db.admin.runCommand(
  {
      setAuditConfig: 1,
      filter:
      {
          atype: "authCheck",
          "param.command":
          {
              $in: ["find", "insert", "delete", "update", "findandmodify"]
          }
      },
      auditAuthorizationSuccess: true
  }
)

var db = db.getSiblingDB('pocchatbot');

db.createCollection('customers_data')

db.customers_data.insert({
  first_name: "Peter",
  last_name: "Doe",
  credit_score: 750,
  married: 1,
  cars_owned: 2,
  kids_number: 3,
  credit_card_owned: 1,
  annual_salary: 80000,
  months_ago_quoted: 6,
  has_a_house: 1
});

db.customers_data.insert({
  first_name: "Denis",
  last_name: "Baciu",
  credit_score: 900,
  married: 1,
  cars_owned: 2,
  kids_number: 3,
  credit_card_owned: 1,
  annual_salary: 55000,
  months_ago_quoted: 6,
  has_a_house: 1
});

db.customers_data.insert({
  first_name: "John",
  last_name: "Smith",
  credit_score: 650,
  married: 0,
  cars_owned: 1,
  kids_number: 0,
  credit_card_owned: 1,
  annual_salary: 60000,
  months_ago_quoted: 2,
  has_a_house: 0
});

db.customers_data.insert({
  first_name: "Jane",
  last_name: "Johnson",
  credit_score: 800,
  married: 1,
  cars_owned: 2,
  kids_number: 2,
  credit_card_owned: 0,
  annual_salary: 95000,
  months_ago_quoted: 3,
  has_a_house: 1
});

db.customers_data.insert({
  first_name: "Emily",
  last_name: "Taylor",
  credit_score: 710,
  married: 0,
  cars_owned: 1,
  kids_number: 0,
  credit_card_owned: 0,
  annual_salary: 55000,
  months_ago_quoted: 1,
  has_a_house: 0
});

db.customers_data.insert({
  first_name: "Robert",
  last_name: "Martin",
  credit_score: 780,
  married: 1,
  cars_owned: 2,
  kids_number: 3,
  credit_card_owned: 1,
  annual_salary: 125000,
  months_ago_quoted: 5,
  has_a_house: 1
});