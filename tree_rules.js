const decisionTree = {
  "feature": "Calories_Burned",
  "threshold": 464.0,
  "left": {
    "feature": "BMI",
    "threshold": 20.09000015258789,
    "left": {
      "feature": "Resting_BPM",
      "threshold": 58.5,
      "left": {
        "class": "Yoga"
      },
      "right": {
        "feature": "Water_Intake (liters)",
        "threshold": 2.149999976158142,
        "left": {
          "feature": "Session_Duration (hours)",
          "threshold": 0.6649999916553497,
          "left": {
            "class": "HIIT"
          },
          "right": {
            "feature": "BMI",
            "threshold": 19.039999961853027,
            "left": {
              "class": "Yoga"
            },
            "right": {
              "class": "Cardio"
            }
          }
        },
        "right": {
          "feature": "Max_BPM",
          "threshold": 183.5,
          "left": {
            "feature": "Workout_Frequency (days/week)",
            "threshold": 2.5,
            "left": {
              "class": "Cardio"
            },
            "right": {
              "feature": "Max_BPM",
              "threshold": 179.5,
              "left": {
                "feature": "Max_BPM",
                "threshold": 169.5,
                "left": {
                  "class": "Strength"
                },
                "right": {
                  "class": "Cardio"
                }
              },
              "right": {
                "class": "Strength"
              }
            }
          },
          "right": {
            "class": "Yoga"
          }
        }
      }
    },
    "right": {
      "feature": "HR_Burn_Ratio",
      "threshold": 2.396525025367737,
      "left": {
        "feature": "Avg_BPM",
        "threshold": 135.5,
        "left": {
          "feature": "Weight (kg)",
          "threshold": 75.0999984741211,
          "left": {
            "feature": "Fat_Percentage",
            "threshold": 34.64999961853027,
            "left": {
              "class": "Cardio"
            },
            "right": {
              "class": "HIIT"
            }
          },
          "right": {
            "feature": "Age",
            "threshold": 29.5,
            "left": {
              "feature": "BMI_Class",
              "threshold": 2.5,
              "left": {
                "class": "Cardio"
              },
              "right": {
                "class": "Yoga"
              }
            },
            "right": {
              "class": "HIIT"
            }
          }
        },
        "right": {
          "feature": "Resting_BPM",
          "threshold": 66.0,
          "left": {
            "feature": "HR_Burn_Ratio",
            "threshold": 2.2969974279403687,
            "left": {
              "feature": "Weight (kg)",
              "threshold": 55.04999923706055,
              "left": {
                "class": "Yoga"
              },
              "right": {
                "feature": "Workout_Frequency (days/week)",
                "threshold": 2.5,
                "left": {
                  "class": "Cardio"
                },
                "right": {
                  "class": "Strength"
                }
              }
            },
            "right": {
              "class": "Yoga"
            }
          },
          "right": {
            "class": "Strength"
          }
        }
      },
      "right": {
        "class": "Cardio"
      }
    }
  },
  "right": {
    "feature": "Calories_Burned",
    "threshold": 493.0,
    "left": {
      "feature": "Max_BPM",
      "threshold": 185.5,
      "left": {
        "feature": "Height (m)",
        "threshold": 1.534999966621399,
        "left": {
          "class": "HIIT"
        },
        "right": {
          "feature": "Water_Intake (liters)",
          "threshold": 3.3000000715255737,
          "left": {
            "class": "Strength"
          },
          "right": {
            "class": "Cardio"
          }
        }
      },
      "right": {
        "feature": "Workout_Frequency (days/week)",
        "threshold": 2.5,
        "left": {
          "class": "Yoga"
        },
        "right": {
          "class": "Strength"
        }
      }
    },
    "right": {
      "feature": "HR_Burn_Ratio",
      "threshold": 8.654695987701416,
      "left": {
        "feature": "Session_Duration (hours)",
        "threshold": 1.875,
        "left": {
          "feature": "Calories_Burned",
          "threshold": 1445.5,
          "left": {
            "feature": "Fat_Percentage",
            "threshold": 31.34999942779541,
            "left": {
              "feature": "Weight (kg)",
              "threshold": 64.14999771118164,
              "left": {
                "feature": "Fat_Percentage",
                "threshold": 16.000000476837158,
                "left": {
                  "feature": "BMI",
                  "threshold": 25.545000076293945,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 161.5,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "class": "Strength"
                  }
                },
                "right": {
                  "feature": "Max_BPM",
                  "threshold": 176.5,
                  "left": {
                    "feature": "Fat_Percentage",
                    "threshold": 17.75,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  },
                  "right": {
                    "feature": "Fat_Percentage",
                    "threshold": 30.84999942779541,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  }
                }
              },
              "right": {
                "feature": "Weight (kg)",
                "threshold": 125.4000015258789,
                "left": {
                  "feature": "HR_Burn_Ratio",
                  "threshold": 3.6840741634368896,
                  "left": {
                    "feature": "Weight (kg)",
                    "threshold": 71.69999694824219,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  },
                  "right": {
                    "feature": "BMI",
                    "threshold": 31.304999351501465,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  }
                },
                "right": {
                  "feature": "Resting_BPM",
                  "threshold": 65.0,
                  "left": {
                    "feature": "Resting_BPM",
                    "threshold": 57.5,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  },
                  "right": {
                    "feature": "Water_Intake (liters)",
                    "threshold": 2.399999976158142,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                }
              }
            },
            "right": {
              "feature": "Max_BPM",
              "threshold": 178.5,
              "left": {
                "feature": "Max_BPM",
                "threshold": 166.5,
                "left": {
                  "feature": "BMI",
                  "threshold": 27.295000076293945,
                  "left": {
                    "feature": "Fat_Percentage",
                    "threshold": 32.10000038146973,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  },
                  "right": {
                    "class": "HIIT"
                  }
                },
                "right": {
                  "feature": "Avg_BPM",
                  "threshold": 126.5,
                  "left": {
                    "feature": "Avg_BPM",
                    "threshold": 122.5,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  },
                  "right": {
                    "feature": "Height (m)",
                    "threshold": 1.7599999904632568,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  }
                }
              },
              "right": {
                "feature": "Session_Duration (hours)",
                "threshold": 1.2400000095367432,
                "left": {
                  "feature": "Weight (kg)",
                  "threshold": 57.60000038146973,
                  "left": {
                    "feature": "Avg_BPM",
                    "threshold": 152.5,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "feature": "Resting_BPM",
                    "threshold": 64.5,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  }
                },
                "right": {
                  "feature": "Avg_BPM",
                  "threshold": 125.5,
                  "left": {
                    "feature": "Resting_BPM",
                    "threshold": 63.0,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  },
                  "right": {
                    "feature": "Age",
                    "threshold": 51.0,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                }
              }
            }
          },
          "right": {
            "class": "HIIT"
          }
        },
        "right": {
          "feature": "Age",
          "threshold": 53.0,
          "left": {
            "feature": "Fat_Percentage",
            "threshold": 13.300000190734863,
            "left": {
              "feature": "BMI",
              "threshold": 25.234999656677246,
              "left": {
                "feature": "Session_Duration (hours)",
                "threshold": 1.9049999713897705,
                "left": {
                  "class": "Cardio"
                },
                "right": {
                  "class": "Strength"
                }
              },
              "right": {
                "class": "HIIT"
              }
            },
            "right": {
              "feature": "Avg_BPM",
              "threshold": 129.5,
              "left": {
                "feature": "Age",
                "threshold": 48.5,
                "left": {
                  "class": "Strength"
                },
                "right": {
                  "class": "Yoga"
                }
              },
              "right": {
                "feature": "Height (m)",
                "threshold": 1.5850000381469727,
                "left": {
                  "feature": "Session_Duration (hours)",
                  "threshold": 1.9450000524520874,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 192.5,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  },
                  "right": {
                    "class": "Yoga"
                  }
                },
                "right": {
                  "class": "Yoga"
                }
              }
            }
          },
          "right": {
            "class": "Cardio"
          }
        }
      },
      "right": {
        "feature": "HR_Burn_Ratio",
        "threshold": 9.721386432647705,
        "left": {
          "feature": "HR_Burn_Ratio",
          "threshold": 9.348440170288086,
          "left": {
            "feature": "Height (m)",
            "threshold": 1.550000011920929,
            "left": {
              "class": "Yoga"
            },
            "right": {
              "feature": "BMI",
              "threshold": 32.98499870300293,
              "left": {
                "feature": "Resting_BPM",
                "threshold": 72.5,
                "left": {
                  "class": "Strength"
                },
                "right": {
                  "feature": "Calories_Burned",
                  "threshold": 1571.5,
                  "left": {
                    "class": "Strength"
                  },
                  "right": {
                    "class": "HIIT"
                  }
                }
              },
              "right": {
                "class": "HIIT"
              }
            }
          },
          "right": {
            "feature": "BMI_Class",
            "threshold": 2.0,
            "left": {
              "class": "Cardio"
            },
            "right": {
              "class": "Strength"
            }
          }
        },
        "right": {
          "class": "HIIT"
        }
      }
    }
  }
};
const workoutTypes = ["Cardio", "HIIT", "Strength", "Yoga"];
