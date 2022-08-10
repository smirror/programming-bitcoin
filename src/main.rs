mod ecc;

fn main() {
    let a = ecc::FieldElement::init(7, 13);
    let b = ecc::FieldElement::init(6, 13);
    let c = ecc::FieldElement::init(13, 13);
    let d = ecc::FieldElement::init(-1, 13);
    println!("{:?}, {:?}", a, b);
    println!("{}", a == b);
    println!("{}", a == a);
    println!("{}", a.add(&b) == c);
    println!("{}", b.sub(&a) == d);
}
