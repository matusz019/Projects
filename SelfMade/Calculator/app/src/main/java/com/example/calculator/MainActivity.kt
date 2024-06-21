package com.example.calculator

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import kotlin.math.abs

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val resultTextView = findViewById<TextView>(R.id.resultTextView)

        val clearButton = findViewById<Button>(R.id.clearButton)
        val absButton = findViewById<Button>(R.id.absButton)
        val percentButton = findViewById<Button>(R.id.percentButton)
        val divButton = findViewById<Button>(R.id.divButton)
        val sevenButton = findViewById<Button>(R.id.sevenButton)
        val eightButton = findViewById<Button>(R.id.eightButton)
        val nineButton = findViewById<Button>(R.id.nineButton)
        val multiButton = findViewById<Button>(R.id.multiButton)
        val fourButton = findViewById<Button>(R.id.fourButton)
        val fiveButton = findViewById<Button>(R.id.fiveButton)
        val sixButton = findViewById<Button>(R.id.sixButton)
        val minButton = findViewById<Button>(R.id.minButton)
        val oneButton = findViewById<Button>(R.id.oneButton)
        val twoButton = findViewById<Button>(R.id.twoButton)
        val threeButton = findViewById<Button>(R.id.threeButton)
        val plusButton = findViewById<Button>(R.id.plusButton)
        val zeroButton = findViewById<Button>(R.id.zeroButton)
        val decimalButton = findViewById<Button>(R.id.decimalButton)
        val sumButton = findViewById<Button>(R.id.sumButton)

        val buttons = arrayOf(
            clearButton, absButton, percentButton, divButton,
            sevenButton, eightButton, nineButton, multiButton,
            fourButton, fiveButton, sixButton, minButton,
            oneButton, twoButton, threeButton, plusButton,
            zeroButton, decimalButton, sumButton
        )

        var firstNumber: Double? = null
        var operator: String? = null
        var secondNumber: Double? = null
        var result: Double? = null

        fun handleButtonClick(button: Button) {
            when (button.id) {
                R.id.clearButton -> {
                    resultTextView.text = ""
                    firstNumber = null
                    operator = null
                    secondNumber = null
                    result = null
                }

                R.id.absButton -> {
                    firstNumber = resultTextView.text.toString().toDoubleOrNull() ?: 0.0
                    firstNumber = -firstNumber!!
                    resultTextView.text = firstNumber.toString()

                }

                R.id.percentButton -> {
                    firstNumber = resultTextView.text.toString().toDouble()
                    firstNumber = firstNumber!! / 100
                    resultTextView.text = firstNumber.toString()

                }

                R.id.divButton -> {             //Make sure this works
                    if (firstNumber == null) {
                        firstNumber = resultTextView.text.toString().toDouble()
                        operator = "/"
                        resultTextView.text = ""
                        println(firstNumber)
                    } else {
                        secondNumber = resultTextView.text.toString().toDouble()
                        println(secondNumber)

                    }
                }

                R.id.sevenButton -> {
                    resultTextView.text = resultTextView.text.toString() + "7"
                }
                R.id.eightButton -> {
                    resultTextView.text = resultTextView.text.toString() + "8"
                }
                R.id.nineButton -> {
                    resultTextView.text = resultTextView.text.toString() + "9"
                }
                R.id.multiButton -> {
                    if (firstNumber == null) {
                        firstNumber = resultTextView.text.toString().toDouble()
                        operator = "*"
                        resultTextView.text = ""
                        println(firstNumber)
                    } else {
                        secondNumber = resultTextView.text.toString().toDouble()
                        operator = "*"
                        resultTextView.text = ""
                    }
                }
                R.id.fourButton -> {
                    resultTextView.text = resultTextView.text.toString() + "4"
                }
                R.id.fiveButton -> {
                    resultTextView.text = resultTextView.text.toString() + "5"
                    }
                R.id.sixButton -> {
                    resultTextView.text = resultTextView.text.toString() + "6"
                }
                R.id.minButton -> {
                    if (firstNumber == null) {
                        firstNumber = resultTextView.text.toString().toDouble()
                        operator = "-"
                        resultTextView.text = ""
                        println(firstNumber)
                    } else {
                        secondNumber = resultTextView.text.toString().toDouble()
                        operator = "-"
                        resultTextView.text = ""
                    }
                }
                R.id.oneButton -> {
                    resultTextView.text = resultTextView.text.toString() + "1"
                }
                R.id.twoButton -> {
                    resultTextView.text = resultTextView.text.toString() + "2"
                }
                R.id.threeButton -> {
                    resultTextView.text = resultTextView.text.toString() + "3"
                }
                R.id.plusButton -> {
                    if (firstNumber == null) {
                        firstNumber = resultTextView.text.toString().toDouble()
                        operator = "+"
                        resultTextView.text = ""
                    } else {
                        secondNumber = resultTextView.text.toString().toDouble()
                        operator = "+"
                        resultTextView.text = ""
                    }
                }
                R.id.zeroButton -> {
                    resultTextView.text = resultTextView.text.toString() + "0"
                }
                R.id.decimalButton -> {
                    resultTextView.text = resultTextView.text.toString() + "."
                }

                R.id.sumButton -> {
                    secondNumber = resultTextView.text.toString().toDouble()
                    val results = when (operator) {
                        "+" -> firstNumber!! + secondNumber!!
                        "-" -> firstNumber!! - secondNumber!!
                        "*" -> firstNumber!! * secondNumber!!
                        "/" -> {
                            if (secondNumber != 0.0) {
                                firstNumber!! / secondNumber!!
                            } else {
                                // Handle division by zero error
                                Double.NaN

                            }
                        }
                        else -> {
                            // Handle invalid operator
                            Double.NaN // Or display an error message
                        }
                    }
                    firstNumber = null
                    secondNumber = null
                    resultTextView.text = results.toString()
                }

            }
        }

        buttons.forEach { button -> button.setOnClickListener {
                handleButtonClick(button)
            }
        }
    }
}