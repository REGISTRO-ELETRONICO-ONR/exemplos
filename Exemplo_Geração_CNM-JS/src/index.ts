import * as cdigit from "cdigit";

const cnmGenerator = (cns: string, number: string, book: string) => {
    const register = number.padStart(7, '0');
    const preCnm = cns + book + register;
    const digit = cdigit.mod97_10.compute(preCnm);

    return cns + "." + book + "." + register + "-" + digit;
}

const x = cnmGenerator("999999", "103", "2");

const isCnmValid = (cnm: string) =>  cdigit.mod97_10.validate(cnm);

console.log(x);
console.log(isCnmValid(x));