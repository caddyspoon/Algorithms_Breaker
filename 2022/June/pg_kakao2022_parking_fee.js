function solution(fees, records) {
  const answer = [];
  const info = {};

  records.forEach(record => {
    const [time, carId, isIn] = record.split(" ");
    const convTime = parseInt(time.split(":")[0]) * 60 + parseInt(time.split(":")[1]);

    if (!(carId in info)) {
      info[carId] = [convTime, 23*60 + 59, 0, false];

    } else {
      switch (isIn) {
        case "IN":
          info[carId][0] = convTime;
          info[carId][3] = false;
          break;
        case "OUT":
          info[carId][1] = convTime;
          info[carId][3] = true;
          info[carId][2] += info[carId][1] - info[carId][0];
        default:
          break;
      }
    }

  })

  const [basicTime, basicFee, perTime, perFine] = fees;

  const calFee = (perInfo) => {
    const totalTime = perInfo[2];

    if (totalTime <= basicTime) {
      return basicFee;
    }

    return basicFee + Math.ceil((totalTime - basicTime) / perTime) * perFine;
  };

  const feeInfo = {};

  for (const key in info) {
    if (!info[key][3]) {
      info[key][2] += (23*60 + 59) - info[key][0];
    }

    feeInfo[key] = calFee(info[key]);
  }

  const sortedKey = Object.keys(feeInfo).sort((a, b) => {
    if (parseInt(a) < parseInt(b)) {
      return -1;
    }
  });

  sortedKey.forEach(key => {
    answer.push(feeInfo[key]);
  })

  return answer;
}

const fees = [180, 5000, 10, 600];
const records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"];
const results = [14600, 34400, 5000];

console.log(solution(fees, records));