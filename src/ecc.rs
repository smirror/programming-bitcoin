#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct FieldElement {
    num: u32,
    prime: u32
}

impl FieldElement{
    pub fn init(num: u32, prime: u32) -> FieldElement {
        if num >= prime {
            panic!("num {} not in field range 0 to {}", num, prime - 1);
        }
        FieldElement {
            num: num % prime,
            prime
        }
    }
}