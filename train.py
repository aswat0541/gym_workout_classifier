const decisionTree = {
  "feature": "Fat_Percentage",
  "threshold": 17.65000057220459,
  "left": {
    "feature": "Max_BPM",
    "threshold": 172.5,
    "left": {
      "feature": "Weight (kg)",
      "threshold": 87.89999771118164,
      "left": {
        "feature": "Session_Duration (hours)",
        "threshold": 1.6050000190734863,
        "left": {
          "class": "HIIT"
        },
        "right": {
          "feature": "BMI",
          "threshold": 21.905000686645508,
          "left": {
            "feature": "Water_Intake (liters)",
            "threshold": 3.100000023841858,
            "left": {
              "class": "Cardio"
            },
            "right": {
              "class": "Strength"
            }
          },
          "right": {
            "feature": "Fat_Percentage",
            "threshold": 12.5,
            "left": {
              "feature": "Session_Duration (hours)",
              "threshold": 1.7599999904632568,
              "left": {
                "feature": "Height (m)",
                "threshold": 1.9249999523162842,
                "left": {
                  "class": "Cardio"
                },
                "right": {
                  "feature": "Max_BPM",
                  "threshold": 160.5,
                  "left": {
                    "class": "Yoga"
                  },
                  "right": {
                    "class": "HIIT"
                  }
                }
              },
              "right": {
                "class": "HIIT"
              }
            },
            "right": {
              "feature": "Weight (kg)",
              "threshold": 63.70000076293945,
              "left": {
                "feature": "Age",
                "threshold": 31.5,
                "left": {
                  "class": "Yoga"
                },
                "right": {
                  "class": "HIIT"
                }
              },
              "right": {
                "class": "Strength"
              }
            }
          }
        }
      },
      "right": {
        "feature": "Workout_Frequency (days/week)",
        "threshold": 4.5,
        "left": {
          "class": "Cardio"
        },
        "right": {
          "class": "Strength"
        }
      }
    },
    "right": {
      "feature": "BMI",
      "threshold": 33.1200008392334,
      "left": {
        "feature": "Session_Duration (hours)",
        "threshold": 1.9049999713897705,
        "left": {
          "feature": "Avg_BPM",
          "threshold": 159.0,
          "left": {
            "feature": "Weight (kg)",
            "threshold": 85.04999923706055,
            "left": {
              "feature": "Weight (kg)",
              "threshold": 82.5999984741211,
              "left": {
                "feature": "Fat_Percentage",
                "threshold": 17.300000190734863,
                "left": {
                  "feature": "Avg_BPM",
                  "threshold": 126.0,
                  "left": {
                    "feature": "Session_Duration (hours)",
                    "threshold": 1.5450000166893005,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  },
                  "right": {
                    "feature": "Weight (kg)",
                    "threshold": 81.20000076293945,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  }
                },
                "right": {
                  "feature": "Resting_BPM",
                  "threshold": 62.5,
                  "left": {
                    "class": "HIIT"
                  },
                  "right": {
                    "class": "HIIT"
                  }
                }
              },
              "right": {
                "feature": "Resting_BPM",
                "threshold": 55.0,
                "left": {
                  "class": "Yoga"
                },
                "right": {
                  "class": "HIIT"
                }
              }
            },
            "right": {
              "feature": "Age",
              "threshold": 37.5,
              "left": {
                "feature": "Avg_BPM",
                "threshold": 150.5,
                "left": {
                  "feature": "Weight (kg)",
                  "threshold": 86.79999923706055,
                  "left": {
                    "feature": "Fat_Percentage",
                    "threshold": 13.549999713897705,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  },
                  "right": {
                    "feature": "BMI_Class",
                    "threshold": 1.5,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  }
                },
                "right": {
                  "feature": "Max_BPM",
                  "threshold": 185.0,
                  "left": {
                    "class": "HIIT"
                  },
                  "right": {
                    "class": "Strength"
                  }
                }
              },
              "right": {
                "feature": "Resting_BPM",
                "threshold": 72.0,
                "left": {
                  "feature": "Max_BPM",
                  "threshold": 175.0,
                  "left": {
                    "class": "Yoga"
                  },
                  "right": {
                    "class": "Yoga"
                  }
                },
                "right": {
                  "class": "Cardio"
                }
              }
            }
          },
          "right": {
            "feature": "Resting_BPM",
            "threshold": 54.0,
            "left": {
              "class": "Yoga"
            },
            "right": {
              "feature": "Fat_Percentage",
              "threshold": 15.899999618530273,
              "left": {
                "class": "HIIT"
              },
              "right": {
                "class": "Cardio"
              }
            }
          }
        },
        "right": {
          "feature": "Weight (kg)",
          "threshold": 85.8499984741211,
          "left": {
            "feature": "Age",
            "threshold": 51.5,
            "left": {
              "feature": "Height (m)",
              "threshold": 1.5199999809265137,
              "left": {
                "class": "Strength"
              },
              "right": {
                "feature": "Fat_Percentage",
                "threshold": 17.100000381469727,
                "left": {
                  "feature": "Max_BPM",
                  "threshold": 189.0,
                  "left": {
                    "class": "Yoga"
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
              "class": "Cardio"
            }
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
  },
  "right": {
    "feature": "BMI",
    "threshold": 22.22000026702881,
    "left": {
      "feature": "Fat_Percentage",
      "threshold": 22.550000190734863,
      "left": {
        "feature": "Weight (kg)",
        "threshold": 70.45000076293945,
        "left": {
          "feature": "Max_BPM",
          "threshold": 180.5,
          "left": {
            "feature": "Weight (kg)",
            "threshold": 57.35000038146973,
            "left": {
              "feature": "Age",
              "threshold": 23.0,
              "left": {
                "class": "HIIT"
              },
              "right": {
                "feature": "Session_Duration (hours)",
                "threshold": 1.3549999594688416,
                "left": {
                  "class": "Strength"
                },
                "right": {
                  "feature": "Age",
                  "threshold": 54.0,
                  "left": {
                    "feature": "Workout_Frequency (days/week)",
                    "threshold": 3.5,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  },
                  "right": {
                    "class": "Strength"
                  }
                }
              }
            },
            "right": {
              "feature": "Water_Intake (liters)",
              "threshold": 2.1999999284744263,
              "left": {
                "class": "Strength"
              },
              "right": {
                "class": "Strength"
              }
            }
          },
          "right": {
            "feature": "Avg_BPM",
            "threshold": 156.0,
            "left": {
              "feature": "BMI",
              "threshold": 16.114999771118164,
              "left": {
                "feature": "Workout_Frequency (days/week)",
                "threshold": 3.5,
                "left": {
                  "class": "Cardio"
                },
                "right": {
                  "class": "Strength"
                }
              },
              "right": {
                "feature": "BMI",
                "threshold": 20.010000228881836,
                "left": {
                  "feature": "Session_Duration (hours)",
                  "threshold": 1.1200000047683716,
                  "left": {
                    "class": "Yoga"
                  },
                  "right": {
                    "class": "Yoga"
                  }
                },
                "right": {
                  "feature": "BMI",
                  "threshold": 21.46500015258789,
                  "left": {
                    "class": "Cardio"
                  },
                  "right": {
                    "class": "Yoga"
                  }
                }
              }
            },
            "right": {
              "class": "Strength"
            }
          }
        },
        "right": {
          "feature": "Session_Duration (hours)",
          "threshold": 0.7050000131130219,
          "left": {
            "class": "Cardio"
          },
          "right": {
            "feature": "Avg_BPM",
            "threshold": 163.0,
            "left": {
              "class": "Yoga"
            },
            "right": {
              "class": "Strength"
            }
          }
        }
      },
      "right": {
        "feature": "Height (m)",
        "threshold": 1.5850000381469727,
        "left": {
          "feature": "Age",
          "threshold": 20.5,
          "left": {
            "class": "Yoga"
          },
          "right": {
            "feature": "Fat_Percentage",
            "threshold": 26.699999809265137,
            "left": {
              "class": "Yoga"
            },
            "right": {
              "feature": "BMI",
              "threshold": 21.369999885559082,
              "left": {
                "feature": "Water_Intake (liters)",
                "threshold": 1.75,
                "left": {
                  "class": "Yoga"
                },
                "right": {
                  "feature": "Fat_Percentage",
                  "threshold": 32.05000019073486,
                  "left": {
                    "feature": "Workout_Frequency (days/week)",
                    "threshold": 3.5,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "class": "Strength"
                  }
                }
              },
              "right": {
                "feature": "Avg_BPM",
                "threshold": 152.0,
                "left": {
                  "feature": "Session_Duration (hours)",
                  "threshold": 1.2799999713897705,
                  "left": {
                    "class": "HIIT"
                  },
                  "right": {
                    "feature": "Session_Duration (hours)",
                    "threshold": 1.3949999809265137,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  }
                },
                "right": {
                  "class": "Cardio"
                }
              }
            }
          }
        },
        "right": {
          "feature": "BMI",
          "threshold": 12.849999904632568,
          "left": {
            "class": "Cardio"
          },
          "right": {
            "feature": "Session_Duration (hours)",
            "threshold": 1.1749999523162842,
            "left": {
              "feature": "BMI",
              "threshold": 18.369999885559082,
              "left": {
                "feature": "BMI",
                "threshold": 15.764999866485596,
                "left": {
                  "feature": "Age",
                  "threshold": 55.5,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 192.5,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  },
                  "right": {
                    "feature": "Resting_BPM",
                    "threshold": 53.0,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                },
                "right": {
                  "feature": "BMI",
                  "threshold": 17.914999961853027,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 168.0,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "feature": "Session_Duration (hours)",
                    "threshold": 0.8599999845027924,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                }
              },
              "right": {
                "feature": "Session_Duration (hours)",
                "threshold": 0.925000011920929,
                "left": {
                  "feature": "Age",
                  "threshold": 31.5,
                  "left": {
                    "class": "Strength"
                  },
                  "right": {
                    "feature": "Avg_BPM",
                    "threshold": 164.0,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  }
                },
                "right": {
                  "feature": "Weight (kg)",
                  "threshold": 54.60000038146973,
                  "left": {
                    "feature": "Water_Intake (liters)",
                    "threshold": 2.399999976158142,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "feature": "Max_BPM",
                    "threshold": 175.0,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  }
                }
              }
            },
            "right": {
              "feature": "Fat_Percentage",
              "threshold": 22.75,
              "left": {
                "class": "HIIT"
              },
              "right": {
                "feature": "Height (m)",
                "threshold": 1.6950000524520874,
                "left": {
                  "feature": "Fat_Percentage",
                  "threshold": 28.25,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 171.5,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "feature": "Water_Intake (liters)",
                    "threshold": 2.149999976158142,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                },
                "right": {
                  "feature": "Age",
                  "threshold": 25.5,
                  "left": {
                    "feature": "Height (m)",
                    "threshold": 1.7549999952316284,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  },
                  "right": {
                    "feature": "Water_Intake (liters)",
                    "threshold": 1.6500000357627869,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "right": {
      "feature": "Fat_Percentage",
      "threshold": 18.15000057220459,
      "left": {
        "class": "Cardio"
      },
      "right": {
        "feature": "Fat_Percentage",
        "threshold": 31.399999618530273,
        "left": {
          "feature": "BMI",
          "threshold": 22.800000190734863,
          "left": {
            "feature": "Avg_BPM",
            "threshold": 152.5,
            "left": {
              "feature": "Gender_Code",
              "threshold": 0.5,
              "left": {
                "feature": "Session_Duration (hours)",
                "threshold": 1.3149999976158142,
                "left": {
                  "feature": "Avg_BPM",
                  "threshold": 124.5,
                  "left": {
                    "class": "Yoga"
                  },
                  "right": {
                    "class": "Yoga"
                  }
                },
                "right": {
                  "class": "HIIT"
                }
              },
              "right": {
                "feature": "Weight (kg)",
                "threshold": 64.25,
                "left": {
                  "feature": "Avg_BPM",
                  "threshold": 138.0,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 180.5,
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
                },
                "right": {
                  "feature": "BMI",
                  "threshold": 22.324999809265137,
                  "left": {
                    "feature": "Resting_BPM",
                    "threshold": 71.5,
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
                }
              }
            },
            "right": {
              "feature": "Gender_Code",
              "threshold": 0.5,
              "left": {
                "class": "HIIT"
              },
              "right": {
                "class": "HIIT"
              }
            }
          },
          "right": {
            "feature": "Weight (kg)",
            "threshold": 128.6999969482422,
            "left": {
              "feature": "Avg_BPM",
              "threshold": 139.5,
              "left": {
                "feature": "Age",
                "threshold": 19.5,
                "left": {
                  "feature": "Workout_Frequency (days/week)",
                  "threshold": 3.5,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 193.0,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  },
                  "right": {
                    "class": "Strength"
                  }
                },
                "right": {
                  "feature": "Fat_Percentage",
                  "threshold": 23.449999809265137,
                  "left": {
                    "feature": "Max_BPM",
                    "threshold": 196.0,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  },
                  "right": {
                    "feature": "Age",
                    "threshold": 26.5,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  }
                }
              },
              "right": {
                "feature": "Water_Intake (liters)",
                "threshold": 1.8499999642372131,
                "left": {
                  "feature": "Age",
                  "threshold": 25.5,
                  "left": {
                    "feature": "Session_Duration (hours)",
                    "threshold": 1.300000011920929,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  },
                  "right": {
                    "feature": "Resting_BPM",
                    "threshold": 70.0,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Yoga"
                    }
                  }
                },
                "right": {
                  "feature": "Age",
                  "threshold": 58.5,
                  "left": {
                    "feature": "Age",
                    "threshold": 18.5,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  },
                  "right": {
                    "feature": "Weight (kg)",
                    "threshold": 122.80000305175781,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "HIIT"
                    }
                  }
                }
              }
            },
            "right": {
              "class": "Yoga"
            }
          }
        },
        "right": {
          "feature": "Age",
          "threshold": 22.5,
          "left": {
            "feature": "BMI",
            "threshold": 24.390000343322754,
            "left": {
              "class": "HIIT"
            },
            "right": {
              "class": "Strength"
            }
          },
          "right": {
            "feature": "Weight (kg)",
            "threshold": 74.70000076293945,
            "left": {
              "feature": "Age",
              "threshold": 49.5,
              "left": {
                "feature": "Avg_BPM",
                "threshold": 129.5,
                "left": {
                  "feature": "Height (m)",
                  "threshold": 1.5299999713897705,
                  "left": {
                    "class": "HIIT"
                  },
                  "right": {
                    "feature": "Water_Intake (liters)",
                    "threshold": 2.099999964237213,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  }
                },
                "right": {
                  "feature": "Age",
                  "threshold": 44.0,
                  "left": {
                    "feature": "Session_Duration (hours)",
                    "threshold": 0.6850000023841858,
                    "left": {
                      "class": "Yoga"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  },
                  "right": {
                    "feature": "Session_Duration (hours)",
                    "threshold": 0.7950000166893005,
                    "left": {
                      "class": "Cardio"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  }
                }
              },
              "right": {
                "feature": "Age",
                "threshold": 53.0,
                "left": {
                  "feature": "BMI",
                  "threshold": 30.839999198913574,
                  "left": {
                    "class": "HIIT"
                  },
                  "right": {
                    "class": "Cardio"
                  }
                },
                "right": {
                  "class": "Cardio"
                }
              }
            },
            "right": {
              "feature": "Height (m)",
              "threshold": 1.6150000095367432,
              "left": {
                "feature": "Max_BPM",
                "threshold": 179.5,
                "left": {
                  "class": "HIIT"
                },
                "right": {
                  "feature": "Water_Intake (liters)",
                  "threshold": 2.0,
                  "left": {
                    "class": "Yoga"
                  },
                  "right": {
                    "class": "Yoga"
                  }
                }
              },
              "right": {
                "feature": "Water_Intake (liters)",
                "threshold": 1.699999988079071,
                "left": {
                  "class": "HIIT"
                },
                "right": {
                  "feature": "Resting_BPM",
                  "threshold": 61.5,
                  "left": {
                    "feature": "Water_Intake (liters)",
                    "threshold": 1.899999976158142,
                    "left": {
                      "class": "Strength"
                    },
                    "right": {
                      "class": "Strength"
                    }
                  },
                  "right": {
                    "feature": "Max_BPM",
                    "threshold": 172.0,
                    "left": {
                      "class": "HIIT"
                    },
                    "right": {
                      "class": "Cardio"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
};
const workoutTypes = ["Cardio", "HIIT", "Strength", "Yoga"];
