<?php
error_reporting(E_ALL);

//$lines = file('trial.txt');
$lines = file('input.txt');
$rules = [];
foreach ($lines as $line) {
   if (trim($line) == '') break;
   parseRule(trim($line));
}

$range = [
   'x' => [ 1, 4000 ],
   'm' => [ 1, 4000 ],
   'a' => [ 1, 4000 ],
   's' => [ 1, 4000 ],
];

$validRanges = [];

process('in', $range);

$sum = 0;
foreach ($validRanges as $range) {
   $sum += nrcomb($range);
}
printf("sum=%d\n", $sum);

function parseRule($rule) {
   global $rules;
   if (preg_match('/^([a-z]+){(.*)}$/', $rule, $matches)) {
      $id = $matches[1];
      $eqs = [];
      $parts = explode(',', $matches[2]);
      foreach ($parts as $part) {
         if (preg_match('/^([xmas])([<>])([0-9]+):(.*)$/', $part, $matches2)) {
            $eq = [
               'prop' => $matches2[1],
               'comp' => $matches2[2],
               'value' => $matches2[3],
               'next' => $matches2[4],
            ];
            $eqs[] = $eq;
         } else {
            $eqs[] = $part;
         }
      }
      $rules[$id] = $eqs;
   }
}

function process($id, $range) {
   global $rules;
   global $validRanges;
   
   if (!isset($rules[$id])) {
      if ($id == 'A') $validRanges[] = $range;
      return;
   }
   
   foreach ($rules[$id] as $part) {
      if (!is_array($part)) return process($part, $range);
      
      //printf("\n");
      //showrange($range);
      //printf("%s %s %s\n", $part['prop'], $part['comp'], $part['value']);
      if ($part['comp'] == '<') {
         $valid = $range;
         $valid[$part['prop']][0] = min($valid[$part['prop']][0], $part['value']-1);
         $valid[$part['prop']][1] = min($valid[$part['prop']][1], $part['value']-1);
         $range[$part['prop']][0] = max($range[$part['prop']][0], $part['value']);
         $range[$part['prop']][1] = max($range[$part['prop']][1], $part['value']);

         //showrange($valid);
         //showrange($range);
         
         process($part['next'], $valid);

      } else {
         $valid = $range;
         $valid[$part['prop']][0] = max($valid[$part['prop']][0], $part['value']+1);
         $valid[$part['prop']][1] = max($valid[$part['prop']][1], $part['value']+1);
         $range[$part['prop']][0] = min($range[$part['prop']][0], $part['value']);
         $range[$part['prop']][1] = min($range[$part['prop']][1], $part['value']);

         //showrange($valid);
         //showrange($range);

         process($part['next'], $valid);

      }
   }
   printf("End of rule?!\n");
   return '?';
}

function showrange($range) {
   foreach ($range as $prop => $v) {
      printf("%s: %d .. %d\n", $prop, $v[0], $v[1]);
   }
}

function nrcomb($range) {
   $nr = 1;
   foreach ($range as $prop => $v) {
      $nr *= ($v[1] - $v[0] + 1);
   }
   return $nr;
}