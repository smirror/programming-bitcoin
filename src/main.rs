mod ecc;

fn main() {
    let a = ecc::FieldElement::init(7, 13);
    let b = ecc::FieldElement::init(6, 13);
    println!("{:?}, {:?}", a, b);
    println!("{}", a == b);
    println!("{}", a == a);
}
