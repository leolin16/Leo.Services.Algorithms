const dayOrderInAYear = require("./dayOrderInAYear");

test("dayOrderInAYear('19841112') returns 317", () => {
  expect(dayOrderInAYear.dayOrderInAYear("19841112")).toEqual(317);
  expect(dayOrderInAYear.monthName(11)).toEqual("Nov");
});

test("dayOrderInAYear('20200322') returns 82", () => {
  expect(dayOrderInAYear.dayOrderInAYear("20200322")).toEqual(82);
  expect(dayOrderInAYear.monthName(3)).toEqual("Mar");
});

test("dayOrderInAYear('20200122') returns 22", () => {
  expect(dayOrderInAYear.dayOrderInAYear("20200122")).toEqual(22);
  expect(dayOrderInAYear.monthName("01")).toEqual("Jan");
});
