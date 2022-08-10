#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct FieldElement {
    num: isize,
    prime:  isize,
}

impl FieldElement{
    pub fn init(num: isize, prime: isize) -> FieldElement {
        // if num >= prime {
        //     panic!("num {} not in field range 0 to {}", num, prime - 1);
        // }
        FieldElement {
            num: num % prime,
            prime
        }
    }

    pub fn add(&self, other: &FieldElement) -> FieldElement {
        if &self.prime != &other.prime {
            panic!("cannot add elements from different prime fields");
        }
        FieldElement::init(self.num + other.num, self.prime)
    }

    pub fn sub(&self, other: &FieldElement) -> FieldElement {
        if &self.prime != &other.prime {
            panic!("cannot subtract elements from different prime fields");
        }
        FieldElement::init(self.num - other.num, self.prime)
    }

    pub fn mul(&self, other: &FieldElement) -> FieldElement {
        if &self.prime != &other.prime {
            panic!("cannot multiply elements from different prime fields");
        }
        FieldElement::init(self.num * other.num, self.prime)
    }

    pub fn pow(&self, exp: u32) -> FieldElement {
        FieldElement::init(self.num.pow(exp), self.prime)
    }
}

#[cfg(test)]
mod tests{
    use crate::ecc::FieldElement;

    #[test]
    fn test_partial_eq(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        assert_eq!(a == b, false);
        assert_eq!(a != b,true);
    }

    #[test]
    fn ex1_1(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        assert_eq!(a != b,true);
    }

    #[test]
    fn test_eq(){
        let a = FieldElement::init(7, 13);
        let b = FieldElement::init(6, 13);
        assert_eq!(a == a, true);
    }

    #[test]
    fn ex1_2_1(){
        let a = FieldElement::init(44, 57);
        let b = FieldElement::init(33, 57);
        let c = FieldElement::init(77, 57);
        assert_eq!(a.add(&b), c);
    }

    #[test]
    fn ex1_2_2(){
        let a = FieldElement::init(9, 57);
        let b = FieldElement::init(29, 57);
        let c = FieldElement::init(-20, 57);
        assert_eq!(a.sub(&b), c);
    }

    #[test]
    fn ex1_2_3(){
        let a = FieldElement::init(17, 57);
        let b = FieldElement::init(42, 57);
        let c = FieldElement::init(49, 57);
        let d = FieldElement::init(108, 57);
        assert_eq!(a.add(&b).add(&c), d);
    }

    #[test]
    fn ex1_2_4(){
        let a = FieldElement::init(52, 57);
        let b = FieldElement::init(30, 57);
        let c = FieldElement::init(38, 57);
        let d = FieldElement::init(-16, 57);
        assert_eq!(a.sub(&b).sub(&c), d);
    }

}
