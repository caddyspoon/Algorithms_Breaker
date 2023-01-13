const convertDate = (date) => {
  const dateInfo = date.split(".").map((elm) => Number(elm));
  return (dateInfo[0] - 2000) * 12 * 28 + dateInfo[1] * 28 + dateInfo[2];
};

const solution = (today, terms, privacies) => {
  const result = [];

  const _today = convertDate(today);

  policyInfo = {};
  terms.map((term) => {
    const [policyName, month] = term.split(" ");
    policyInfo[policyName] = Number(month);
  });

  privacies.map((infos, idx) => {
    const [dateInfo, policy] = infos.split(" ");
    const dateConverted = convertDate(dateInfo) + policyInfo[policy] * 28 - 1;

    if (_today > dateConverted) {
      result.push(idx + 1);
    }
  });

  return result;
};
