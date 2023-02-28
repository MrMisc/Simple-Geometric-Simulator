use rand::distributions::Uniform;
use rand::{thread_rng, Rng};


extern crate serde;
extern crate serde_json;
use serde::{Deserialize, Serialize};


// use std::error::Error;
use std::fs::File;
use std::io::Read;
use std::time::{Duration, Instant};

// #[derive(Deserialize)]
#[derive(Serialize, Deserialize, Debug)]
pub struct Params {
    items: Vec<String>,
    probabilities: Vec<f64>,
    number:u8, //Number of outputted items per roll
    trials:u32, //Number of repeated trials
}

fn trial(prob: &[f64]) -> usize {
    let mut rng = thread_rng();
    let roll = Uniform::new(0.0, 1.0);
    let rollnumber: f64 = rng.sample(roll);
    let mut rollover: f64 = 0.0;
    let mut count: u8 = 0;
    for i in prob{
        rollover+=i;
        if rollnumber<rollover{
            break
        }
        count+=1;
    }
    count as usize
}

fn main(){
    let mut file = File::open("./output.json").unwrap();
    let mut buff = String::new();
    file.read_to_string(&mut buff).unwrap();

    let data: Params = serde_json::from_str(&buff).unwrap();

    // let mut record: Vec<Vec<String>> = Vec::new();
    let num_record:&mut [u32] = &mut vec![0;data.items.len()];
    for _j in 0..data.trials as usize{//for every trial...
        // let mut rolls:Vec<String> = Vec::new();
        // let mut roll_num: &mut [u32] = &mut vec![0;data.items.len()];
        for _k in 0..data.number as usize{
            let no: usize = trial(&data.probabilities);
            // rolls.push(data.items[no].clone());
            num_record[no]+=1;
            // roll_num[no]+=1;
            // println!("{:?}",num_record);
            // println!("----------");
        }
        println!("{:?}",num_record);
        // record.push(rolls)
    }

    // record = record.iter().map(|x| data.items[x]).collect();
    // println!("{:?}",record);
    // println!("{:?}",num_record);
    println!("{:?}",data.items);
    // assert_eq!(data.items.len(),num_record.len());
}
